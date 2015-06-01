# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  project_name = 'myblog'
  $memory = 1024
  $cpus = 2
  
  config.vm.provider :virtualbox do |vb|
    config.vm.box = "hashicorp/precise64"
    vb.memory = $memory
    vb.cpus = $cpus
  end

  config.vm.provider :parallels do |prl|
    config.vm.box = "parallels/ubuntu-14.04"
    prl.memory = $memory
    prl.cpus = $cpus
  end

  config.vm.synced_folder ".", "/home/vagrant/#{project_name}"
  config.vm.provision "shell", path: "extras/vagrant.sh", :args => "#{project_name}"
end
