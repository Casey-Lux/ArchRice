# ArchRice

Configuración (*rice*) técnica y minimalista para **Arch Linux**, orientada a estabilidad, productividad y mantenimiento a largo plazo.
El repositorio centraliza archivos de configuración y scripts para desplegar un entorno de trabajo coherente basado en herramientas clásicas del ecosistema Linux.

> Filosofía: simple, explícito, reproducible.

---

## Objetivo del proyecto

* Proveer una **base funcional** para un escritorio en Arch Linux.
* Evitar configuraciones frágiles o excesivamente experimentales.
* Facilitar reinstalaciones y migraciones del sistema.
* Servir como punto de partida para personalización futura.

Este rice **no pretende ser universal** ni "plug-and-play" para todos los usuarios.

---

## Componentes incluidos

### Gestor de ventanas y entorno gráfico

* **Qtile**
  Gestor de ventanas en mosaico, configurado en Python.

* **Picom**
  Compositor ligero para sombras y transparencia controlada.

* **Xinit**
  Inicio manual del servidor X, sin display manager.

### Terminal y shell

* **Alacritty**
  Terminal acelerada por GPU con configuración personalizada.

* **Zsh**
  Shell interactiva con alias y ajustes prácticos.

* **Tmux**
  Multiplexor de terminal para sesiones persistentes.

### Utilidades

* **Rofi**
  Lanzador de aplicaciones y menús rápidos.

* **lf**
  Administrador de archivos en terminal.

---

## Estructura del repositorio

```text
ArchRice/
├── alacritty/        # Configuración del terminal
├── picom/            # Compositor
├── qtile/            # Configuración del window manager
├── rofi/             # Lanzador de aplicaciones
├── tmux/             # Multiplexor de terminal
├── zsh/              # Shell
├── xinit/            # Inicio de X
├── autoinstall.sh    # Script de instalación base
├── notas.txt         # Apuntes y recordatorios
└── README.md         # Este archivo
```

---

## Requisitos

* Arch Linux instalado
* Usuario con privilegios `sudo`
* Conexión a Internet
* Conocimientos básicos de terminal

No se recomienda ejecutar este rice en sistemas productivos sin revisión previa.

---

## Instalación automática

1. Clonar el repositorio:

```sh
git clone https://github.com/Casey-Lux/ArchRice.git
cd ArchRice
```

2. Dar permisos de ejecución al script:

```sh
chmod +x autoinstall.sh
```

3. Ejecutar el instalador:

```sh
sudo ./autoinstall.sh
```

El script instalará paquetes necesarios y copiará las configuraciones correspondientes.

> Nota: el contenido del script debe revisarse antes de ejecutarse.

---

## Instalación manual

Para aplicar configuraciones de forma selectiva:

```sh
cp -r qtile picom rofi tmux $HOME/.config/
cp zsh/.zshrc $HOME/
```

Instalar paquetes requeridos (ejemplo):

```sh
sudo pacman -S qtile picom rofi tmux alacritty zsh
```

Cambiar shell por defecto:

```sh
chsh -s $(which zsh)
```

---

## Uso

* Iniciar entorno gráfico desde TTY:

```sh
startx
```

* Qtile se cargará automáticamente si está configurado en `.xinitrc`.

---

## Mantenimiento

* Mantener Arch actualizado regularmente:

```sh
sudo pacman -Syu
```

* Revisar cambios en Qtile y Picom tras actualizaciones mayores.
* Respaldar `$HOME/.config` antes de modificar configuraciones críticas.

---

## Limitaciones conocidas

* No incluye gestor de login gráfico.
* No incluye temas GTK ni configuración de aplicaciones gráficas pesadas.
* Pensado para X11, no Wayland.

---

## Licencia

Este proyecto incluye una licencia abierta definida en el archivo LICENSE.
Asegúrate de revisar los términos de dicha licencia para entender permisos y restricciones antes de redistribuir o reutilizar el código.

---

## Aviso

Este proyecto recopila configuraciones propias y adaptaciones de recursos públicos.
Úsalo bajo tu propia responsabilidad y adáptalo a tu hardware y flujo de trabajo.

---

