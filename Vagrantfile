$script = <<-'SCRIPT'
echo "Provisioning the VM"
sudo apt-get update -y
sudo apt-get install -y telnet bash-completion wget curl vim ntp
swapoff -a
sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
sudo systemctl restart sshd
sudo systemctl start ntp
sudo timedatectl set-timezone "Asia/Kolkata"
SCRIPT
#sudo sed -i s/^SELINUX=.*$/SELINUX=disabled/ /etc/selinux/config
#sudo date > /etc/vagrant_provisioned_at
# ENV['VAGRANT_DEFAULT_PROVIDER'] = 'libvirt'

Vagrant.configure("2") do |config|
config.vm.provision "shell", inline: $script
config.vm.synced_folder "./", "/home/vagrant/synced_folder", :mount_options => ["dmode=777", "fmode=666"]
  config.vm.define "python" do |prometheus|
    prometheus.vm.box = "ubuntu/bionic64"
    prometheus.vm.hostname = 'prometheus'
    prometheus.vm.network :private_network, bridge: "wlp5s0", ip: "192.168.56.60"
    prometheus.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--memory", 4096]
      v.customize ["modifyvm", :id, "--cpus", 2]
      v.customize ["modifyvm", :id, "--name", "python"]
  end
end
end
