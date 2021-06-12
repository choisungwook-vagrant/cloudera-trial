IMAGE_NAME = "centos/7"
IP = "192.168.25.142"
HOSTNAME = "docker-vagrant"
CPU = 4
RAM = 4096

require 'yaml'

# if File.file?("#{current_dir}/vagrant.yml")
CONFIG = YAML.load_file(File.join(File.dirname(__FILE__), 'config.yml'))


Vagrant.configure("2") do |config|
  config.ssh.insert_key = false

  CONFIG['bootstrap'].each do |bootstrap|
    config.vm.define bootstrap['name'] do |cfg|
      cfg.vm.box = bootstrap['box']
      cfg.vm.network "public_network", ip: bootstrap['ip']
      cfg.vm.hostname = bootstrap['hostname']
      
      cfg.vm.provider "virtualbox" do |v|
        v.memory = bootstrap['memory']
        v.cpus = bootstrap['cpu']
        v.name = bootstrap['hostname']
      end
  
      cfg.vm.provision "shell", inline: <<-SCRIPT
        yum install epel-release -y
        yum install vim git tree wget -y
        sed -i -e 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
        systemctl restart sshd
      SCRIPT
  
      cfg.vm.provision "file", source: "chrony.conf", destination: "chrony.conf"
      cfg.vm.provision "file", source: "configure.sh", destination: "configure.sh"
      cfg.vm.provision "file", source: "install.sh", destination: "install.sh"
      cfg.vm.provision "file", source: "hosts", destination: "hosts"
  
      cfg.vm.provision "shell", inline: "bash configure.sh"
      cfg.vm.provision "shell", inline: "bash install.sh"
    end
  end

  CONFIG['servers'].each do |server|
    config.vm.define server['name'] do |cfg|
      cfg.vm.box = server['box']
      cfg.vm.network "public_network", ip: server['ip']
      cfg.vm.hostname = server['hostname']
      
      cfg.vm.provider "virtualbox" do |v|
        v.memory = server['memory']
        v.cpus = server['cpu']
        v.name = server['hostname']
      end
  
      cfg.vm.provision "shell", inline: <<-SCRIPT
        yum install epel-release -y
        yum install vim git tree wget -y
        sed -i -e 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
        systemctl restart sshd
      SCRIPT
  
      cfg.vm.provision "file", source: "chrony.conf", destination: "chrony.conf"
      cfg.vm.provision "file", source: "configure.sh", destination: "configure.sh"
      cfg.vm.provision "file", source: "hosts", destination: "hosts"
  
      cfg.vm.provision "shell", inline: "bash configure.sh"
    end
  end
end