from compiler import program


def main() -> None:
    prog = '''
        class A {
            int x = 0;
            int input_int(String name) {
                if (name != "") {
                    print("Введите " + name + ": ");
                }
                int a = parseInt(read());
                if (a > 0) {
                    println(a);
                }
                return a;
            }
        }
        class B { }
    '''

    program.execute(prog)


if __name__ == "__main__":
    main()

