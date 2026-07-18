#Ansible adhoc commands
ansible -i inventory all -m "shell" -a "touch filee"
ls -ltr

ansible -i inventory all -m "shell" -a "nproc"
ansible -i inventory all -m "shell" -a "df"
copy one file to other file

# used to runplaybook

ansible-playbook -i inventory first-playbook.yml
