#include <iostream>
#include <fstream>
#include <random>
#include <bitset>
#include <string>


void generate_and_save_128bit_binary() {

    std::random_device rd;
    std::mt19937_64 gen(rd());

    uint64_t part1 = gen();
    uint64_t part2 = gen();

    std::string binary_128 =
        std::bitset<64>(part1).to_string() +
        std::bitset<64>(part2).to_string();


    std::ofstream out_file("Sequence_C.txt");
    if (out_file.is_open()) {
        out_file << binary_128;
        out_file.close();
    }
    else {
        std::cerr << "ERROR";
    }
}

int main() {
    generate_and_save_128bit_binary();

    return 0;
}