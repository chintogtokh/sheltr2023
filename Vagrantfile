# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/artful64"
  config.disksize.size = "30GB"

  # config.vm.box_check_update = false
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 3000, host: 3000
  config.vm.network "forwarded_port", guest: 4000, host: 4000
  config.vm.network "forwarded_port", guest: 5000, host: 5000

  # config.vm.network "private_network", ip: "192.168.33.10"
  # config.vm.network "public_network"

  config.vm.synced_folder "C:/_linux", "/home/vagrant/data",
    # type: "rsync",
    # rsync__auto: true,
    # rsync__exclude: [
    #   '.git*', 'node_modules*',
    #   '*.lnk', '*.cmd', '*.sublime*', '*.sh'
    # ],
    # rsync__verbose: true
    owner: "vagrant",
    group: "vagrant",
    mount_options: ["dmode=777,fmode=777"]
    #type: "smb"

  config.ssh.username = "vagrant"
  config.ssh.password = "vagrant"

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL

  config.vm.provider "virtualbox" do |v|
     v.memory = 4096
     v.cpus = 1
  end
end
