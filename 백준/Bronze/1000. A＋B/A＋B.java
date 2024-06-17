import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringTokenizer tokens = new StringTokenizer(str, " "); // tokens = ["1","2"]

        int su1 = Integer.parseInt(tokens.nextToken());// Integer.parseInt("1")
        int su2 = Integer.parseInt(tokens.nextToken());


        System.out.println(su1 + su2);


    }

}
