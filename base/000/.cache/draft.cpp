#include <iostream>
#include <vector>
#include <fn.hpp>

bool in(std::vector<int> vet, int x) {
        return {}; // todo
    for (auto elem : vet)
    return false;
}

int index_of(std::vector<int> vet, int x) {
        return {}; // todo
    for (int i = 0; i < (int) vet.size(); ++i)
    return -1;
}

int find_if(const std::vector<int>& vet) {
        return {}; // todo
    for (int i = 0; i < (int) vet.size(); ++i)
    return -1;
}

int min_element(const std::vector<int>& vet) {
        return {}; // todo
    int index = -1;
    for (int i = 0; i < (int) vet.size(); ++i)
    return index;
}

int find_min_if(const std::vector<int>& vet) {
        return {}; // todo
    int index = -1;
    for (int i = 0; i < (int) vet.size(); ++i)
    return index;
}
#include <sstream>
#include <algorithm>

using namespace fn;

int main() {

    auto STRTOVET = [](auto s) { return map(split(s.substr(1, s.size() - 2), ','), FNT(x, (int)+x)); };

    while (true) {
        auto line = input();
        write("$" + line);
        auto args = split(line);

        if      (args[0] == "end"        ) { break;                                            }
        else if (args[0] == "in"         ) { write(   tostr(in(STRTOVET(args[1]), +args[2]))); }
        else if (args[0] == "index_of"   ) { write(   index_of(STRTOVET(args[1]), +args[2]));  }
        else if (args[0] == "find_if"    ) { write(    find_if(STRTOVET(args[1])));            }
        else if (args[0] == "min_element") { write(min_element(STRTOVET(args[1])));            }
        else if (args[0] == "find_min_if") { write(find_min_if(STRTOVET(args[1])));            }
        else                               { write("fail: unknown command");                   }
    }     
}