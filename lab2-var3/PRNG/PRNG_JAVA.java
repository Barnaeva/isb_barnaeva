import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class Main {
    public static void generateAndSave128BitBinary() {
        Random random = new Random();
        long part1 = random.nextLong();
        long part2 = random.nextLong();
        String binary128 = String.format("%64s", Long.toBinaryString(part1)).replace(' ', '0')
                        + String.format("%64s", Long.toBinaryString(part2)).replace(' ', '0');
        try (FileWriter writer = new FileWriter("Sequence_Java.txt")) {
            writer.write(binary128);
        } catch (IOException e) {
            System.err.println("ERROR: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        generateAndSave128BitBinary();
    }
}