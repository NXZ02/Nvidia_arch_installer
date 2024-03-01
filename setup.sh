arch_yay() {
    if ! which yay > /dev/null; then
    clear
    sudo pacman -Syu --noconfirm
    sudo pacman -S --needed base-devel git --noconfirm
    git clone https://aur.archlinux.org/yay.git
    cd yay
    makepkg -si  --noconfirm
fi
}

sudo pacman -S --noconfirm tk python-pillow
pip3 install pillow --break-system-packages
clear
echo " Run as  python3 nvidia.py"
echo
