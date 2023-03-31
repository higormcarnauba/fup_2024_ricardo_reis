# Instalando e configurando o tk e o fn.cpp

![](cover.jpg)

## fn.cpp

[LINK](https://raw.githubusercontent.com/senapk/cppaux/master/fn.hpp)

- Opção 1: colocar na pasta /usr/local/include
- Opção 2: colocar na pasta do projeto usando o include entre aspas para indicar que é um arquivo local.

```cpp
#include "fn.hpp"

int main() {
    fn::write("Hello, World!");
    return 0;
}
```

## tk

- baixar o tk [LINK](https://raw.githubusercontent.com/senapk/tk/master/tk.py)
- se estiver no linux, renomear para `tk` e habilitar execução `chmod +x tk`
- baixar o tk e colocar dentro de algum path executável
  - /usr/local/bin
  - ~/bin

```py
$ tk -h
usage: tk [-h] {list,exec,run,build,update,down,gui} ...

options:
  -h, --help            show this help message and exit

subcommands:
```