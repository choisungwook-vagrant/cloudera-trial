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

  config.vm.define CONFIG['server1']['name'] do |cfg|
    cfg.vm.box = CONFIG['server1']['box']
    cfg.vm.network "public_network", ip: CONFIG['server1']['ip']
    cfg.vm.hostname = CONFIG['server1']['hostname']
    
    cfg.vm.provider "virtualbox" do |v|
      v.memory = CONFIG['server1']['memory']
      v.cpus = CONFIG['server1']['cpu']
      v.name = CONFIG['server1']['hostname']
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

  config.vm.define CONFIG['server2']['name'] do |cfg|
    cfg.vm.box = CONFIG['server2']['box']
    cfg.vm.network "public_network", ip: CONFIG['server2']['ip']
    cfg.vm.hostname = CONFIG['server2']['hostname']
    
    cfg.vm.provider "virtualbox" do |v|
      v.memory = CONFIG['server2']['memory']
      v.cpus = CONFIG['server2']['cpu']
      v.name = CONFIG['server2']['hostname']
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

  config.vm.define CONFIG['server3']['name'] do |cfg|
    cfg.vm.box = CONFIG['server3']['box']
    cfg.vm.network "public_network", ip: CONFIG['server3']['ip']
    cfg.vm.hostname = CONFIG['server3']['hostname']
    
    cfg.vm.provider "virtualbox" do |v|
      v.memory = CONFIG['server3']['memory']
      v.cpus = CONFIG['server3']['cpu']
      v.name = CONFIG['server3']['hostname']
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