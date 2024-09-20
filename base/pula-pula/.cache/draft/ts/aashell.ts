import { Trampoline } from "./trampoline";
import { Kid } from "./kid";

function input(): string { let X: any = input; X.L = X.L || require("fs").readFileSync(0).toString().split(/\r?\n/); return X.L.shift(); } // _TEST_ONLY_
// function input(): string { let X: any = input; X.P = X.P || require("readline-sync"); return X.P.question() } // _FREE_ONLY_
function write(text: any, endl="\n") { process.stdout.write("" + text + endl); }

function main() {
    let tr = new Trampoline();

    while (true) {
        write("$", "");
        let line = input();
        write(line); // _TEST_ONLY_
        let args = line.split(" ");

        if      (args[0] == "end"   ) { break                                  }
        else if (args[0] == "show"  ) { write(tr.toString());                  }
        else if (args[0] == "arrive") { tr.arrive(new Kid(args[1], +args[2])); }
        else if (args[0] == "enter" ) { tr.enter();                            }
        else if (args[0] == "leave" ) { tr.leave();                            }
        else if (args[0] == "remove") { let kid = tr.removeKid(args[1]);       }
        else                          { write("fail: comando invalido");       }
    }
}

main();