#include <iostream>
#include <sstream>
#include <vector>

namespace aux {
    double number(std::string text) {
        std::stringstream ss(text);
        double value {};
        if (ss >> value) {
            return value;
        }
        std::cout << "fail: (" << text << ") is not a number\n";
        return 0.0;
    }

    std::vector<std::string> split(std::string line, char delimiter = ' ') {
        std::stringstream ss(line);
        std::vector<std::string> result;
        std::string token;
        while (std::getline(ss, token, delimiter)) {
            result.push_back(token);
        }
        return result;
    }

    template <class T, class FN> std::string join(T container, std::string sep, FN fn) { 
        std::stringstream ss;
        for (auto it = container.begin(); it != container.end(); ++it) {
            ss << (it == container.begin() ? "" : sep) << fn(*it);
        }
        return ss.str();
    }

    template <class T> std::string join(T container, std::string sep = ", ") {
        return join(container, sep, [](auto item) { return item; });
    }

    std::string input() {
        std::string line;
        std::getline(std::cin, line);
        return line;
    }

    template <class T> void write(T data, std::string end = "\n") {
        std::cout << data << end;
    }

    template <class DATA>
    std::string format(std::string format, DATA data) {
        char buffer[100];
        sprintf(buffer, format.c_str(), data);
        return buffer;
    }
}
using namespace aux;

int main() {
    std::vector<int> vet;
    while (true) {
        auto line = input();
        write("$" + line);
        auto args = split(line);

        if      (args[0] == "end")   { break;                                                               }
        else if (args[0] == "push")  { 
            for (size_t i = 1; i < args.size(); ++i) { 
                vet.push_back((int) number(args[i])); 
            } 
        }
        else if (args[0] == "show")  { write("[" + join(vet, ", ") + "]");                                  }
        else if (args[0] == "erase") { vet.erase(vet.begin() + (int) number(args[1]));                      }
        else if (args[0] == "media") {
            double sum = 0;
            for (auto item : vet) {
                sum += item;
            }
            write(format("%.2f", sum / vet.size()));
        }
        else                         { write("fail: invalid command");                                      }
    }
}