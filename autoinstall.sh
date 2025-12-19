#!/bin/bash
set -e

### VARIABLES
REPO_DIR="$(pwd)"
CONFIG_DIR="$HOME/.config"

echo "===> Actualizando sistema"
sudo pacman -Syu --noconfirm

echo "===> Instalando dependencias base"
sudo pacman -S --noconfirm git curl

echo "===> Instalando Xorg"
sudo pacman -S --noconfirm xorg-server xorg-xinit xorg-xrandr

echo "===> Instalando Qtile"
sudo pacman -S --noconfirm qtile python-psutil python-setuptools

echo "===> Preparando directorios"
mkdir -p "$CONFIG_DIR"

echo "===> Copiando configuración de Qtile"
cp -r "$REPO_DIR/qtile" "$CONFIG_DIR/"
[ -f "$CONFIG_DIR/qtile/autostart.sh" ] && chmod +x "$CONFIG_DIR/qtile/autostart.sh"

echo "===> Instalando .xinitrc"
cp "$REPO_DIR/xinit/.xinitrc" "$HOME/.xinitrc"
chmod +x "$HOME/.xinitrc"

echo "===> Instalando programas base para Qtile"
sudo pacman -S --noconfirm \
    picom feh rofi alacritty xterm neovim screenfetch \
    firefox thunar scrot \
    btop lf bat poppler \
    tmux

echo "===> Instalando wallpapers"
if [ ! -d "$HOME/wallpapers" ]; then
    git clone https://github.com/Casey-Lux/wallpapers-Qtile.git /tmp/wallpapers-Qtile
    mkdir -p "$HOME/wallpapers"
    cp -r /tmp/wallpapers-Qtile/wallpapers/* "$HOME/wallpapers/"
    rm -rf /tmp/wallpapers-Qtile
fi

echo "===> Instalando Nerd Fonts"
sudo pacman -S --noconfirm \
    ttf-ubuntu-mono-nerd \
    ttf-nerd-fonts-symbols \
    ttf-fira-code \
	ttf-meslo-nerd

echo "===> Instalando Zsh"
sudo pacman -S --noconfirm zsh
if [ "$SHELL" != "/usr/bin/zsh" ]; then
    sudo chsh -s /usr/bin/zsh "$USER" || true
fi

echo "===> Instalando Oh My Zsh"
if [ ! -d "$HOME/.oh-my-zsh" ]; then
    RUNZSH=no \
    CHSH=no \
    KEEP_ZSHRC=yes \
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
fi

ZSH_CUSTOM="${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}"

echo "===> Instalando plugins de Zsh"
[ ! -d "$ZSH_CUSTOM/plugins/zsh-autosuggestions" ] && \
git clone https://github.com/zsh-users/zsh-autosuggestions \
"$ZSH_CUSTOM/plugins/zsh-autosuggestions"

[ ! -d "$ZSH_CUSTOM/plugins/zsh-syntax-highlighting" ] && \
git clone https://github.com/zsh-users/zsh-syntax-highlighting \
"$ZSH_CUSTOM/plugins/zsh-syntax-highlighting"

echo "===> Instalando tema Powerlevel10k"
[ ! -d "$ZSH_CUSTOM/themes/powerlevel10k" ] && \
git clone https://github.com/romkatv/powerlevel10k.git \
"$ZSH_CUSTOM/themes/powerlevel10k"

echo "===> Copiando configuración de alacritty"
mkdir -p "$CONFIG_DIR/alacritty"
cp "$REPO_DIR/alacritty/alacritty.toml" "$CONFIG_DIR/alacritty/alacritty.toml"

echo "===> Copiando configuración de picom"
mkdir -p "$CONFIG_DIR/picom"
cp "$REPO_DIR/picom/picom.conf" "$CONFIG_DIR/picom/picom.conf"

echo "===> Copiando configuración de Zsh"
cp "$REPO_DIR/zsh/.zshrc" "$HOME/.zshrc"
cp "$REPO_DIR/zsh/.p10k.zsh" "$HOME/.p10k.zsh"

echo "===> Copiando configuración de tmux"
cp "$REPO_DIR/tmux/.tmux.conf" "$HOME/.tmux.conf"

echo "===> Copiando configuración de lf"
mkdir -p "$CONFIG_DIR/lf"
cp -r "$REPO_DIR/lf/"* "$CONFIG_DIR/lf/"
[ -f "$CONFIG_DIR/lf/previewer.sh" ] && chmod +x "$CONFIG_DIR/lf/previewer.sh"

echo "===> Copiando configuración de rofi"
mkdir -p "$CONFIG_DIR/rofi"
cp -r "$REPO_DIR/rofi/"* "$CONFIG_DIR/rofi/"

echo "===> Listo. Reinicia sesión para aplicar Zsh."
