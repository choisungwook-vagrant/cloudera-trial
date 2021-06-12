import chevron
import argparse
from ping3 import ping
from exception import UserDefinedException
import os
from pathlib import Path

# parsing input
parser = argparse.ArgumentParser()
parser.add_argument("--bootstrapIP", type=str, required=True, help="bootstrap IPS")
parser.add_argument("--bootstrapCPU", type=str, required=False, default="4", help="bootstrap CPU")
parser.add_argument("--bootstrapMemory", type=str, required=False, default="4096", help="bootstrap Mmeory") # 4GB
parser.add_argument("--bootstrapDisk", type=str, required=False, default="20GB", help="bootstrap disk")
parser.add_argument("--serverIPS", type=str, required=True, help="server IPS")
parser.add_argument("--serverCPU", type=str, required=False, default="4", help="server CPU")
parser.add_argument("--serverMemory", type=str, required=False, default="16384", help="server Memory") # 16GB
parser.add_argument("--serverDisk", type=str, required=False, default="50GB", help="server Disk") # 50GB
parser.add_argument("--skip", type=str, required=False, default=False, help="skip ping test")
args = parser.parse_args()


def split_args(arguments):
    """
        ","구분자로 split
        리턴: list
    """
    try:
        return arguments.split(",")
    except UserDefinedException as e:
        raise UserDefinedException(f"[-] split_args Error split: {e}")

def generate_template(config):
    '''
        yaml템플릿 생성
    '''
    try:
        with open('template.yml', 'r') as f:
            return chevron.render(f, 
                {
                    'image': config['image'],
                    'name': config['name'],
                    'ip': config['ip'],
                    'memory': config['memory'],
                    'cpu': config['cpu'],
                    'disk': config['disk']
                }
            )
    except Exception as e:
        raise UserDefinedException(f"[-] generate_template Error: {e}")

def create_vagrant_configfile(bootstrap_config, server_configs):
    '''
        vagrant_config파일 생성
        생성위치: ../config.yml
    '''
    
    if not bootstrap_config:
        raise UserDefinedException(f"[-] create_vagrant_configfile Error: bootstrap_config is None")
    if not server_configs or len(server_configs) == 0:
        raise UserDefinedException(f"[-] create_vagrant_configfile Error: server_configs is None")

    try:
        with open('vagrant_template.yml', 'r') as f:
            vagrant_config = chevron.render(f, 
                {
                    'servers': "\n".join(server_configs),
                    'numberOfservers': len(server_configs),
                    'bootstrap': bootstrap_config,
                }
            )

        output_path = os.path.join(Path(os.getcwd()).parent, 'config.yml')
        with open(output_path, 'w') as f:
            f.write(vagrant_config)
    except Exception as e:
        raise UserDefinedException(f"[-] generate_template Error: {e}")

def create_hostsfile(server_IPS):
    '''
        hosts 파일 생성
    '''
    try:    
        with open('hosts_template', 'r') as f:
            hosts = [f"{serverip} cloudrea{idx+1}.network.com" for idx, serverip in enumerate(server_IPS)]
            hostsfile_data = chevron.render(f,
                {
                    "hosts": hosts
                }
            )

        output_path = os.path.join(Path(os.getcwd()).parent, 'hosts')
        print("[*] create hosts file done")
        with open(output_path, 'w') as f:
            f.write(hostsfile_data)
    except Exception as e:
        raise UserDefinedException(f"[-] create hostsfile Error:{e}")

def ping_to_configIP(target):
    """
        ping test
    """
    try:
        result = ping(target)

        return True if result else False
    except Exception as e:
        raise UserDefinedException(f"[-] ping error: {e}")

if __name__=="__main__":
    try:
        vagrant_image = "centos/7"
        bootstrap_IP = args.bootstrapIP
        server_IPS = split_args(args.serverIPS)
        bootstrap_configs = []
        server_configs = []

        print("[*] print IPS")
        print(f"bootstrap: {bootstrap_IP}")
        print(f"serverIPs: {server_IPS}")
        print("\n")

        # # 1. ping test
        if not args.skip:
            print("[*] ping test start")
            if ping_to_configIP(bootstrap_IP):
                raise UserDefinedException(f"bootstrap IP is already exists: {bootstrap_IP}")

            for servesrIP in server_IPS:
                if ping_to_configIP(servesrIP):
                    raise UserDefinedException(f"master IP is already exists: {servesrIP}")

            print("[*] ping test done")
            print("\n")

        # 2. genreate template
        print("[*] generate bootstrap config")
        bootstrap_nodename= f"cloudera-bootstrap"
        bootstrap_config_dict = {
            'image': vagrant_image,
            'name': bootstrap_nodename,
            'ip': args.bootstrapIP,
            'memory': args.bootstrapMemory,
            'cpu': args.bootstrapCPU,
            'disk': args.bootstrapDisk
        }
        bootstrap_config = generate_template(bootstrap_config_dict)
        print("[*] generate bootstrap done")

        print("[*] generate servers config")
        for idx, serverIP in enumerate(server_IPS):
            nodename= f"cloudrea{idx+1}.network.com"
            config = {
                'keyname': nodename,
                'image': vagrant_image,
                'name': nodename,
                'ip': serverIP,
                'memory': args.serverMemory,                
                'cpu': args.serverCPU,
                'disk': args.serverDisk
            }
            server_configs.append(generate_template(config))
        print("[*] generate server config done")

        # 3. create vagrant_config.yml
        create_vagrant_configfile(bootstrap_config, server_configs)

        # 4. hosts파일 생성
        create_hostsfile(server_IPS)

    except Exception as e:
        print(f"error: {e}")
