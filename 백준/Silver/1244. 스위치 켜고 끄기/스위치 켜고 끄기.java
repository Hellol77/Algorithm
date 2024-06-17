import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String switchNumber = br.readLine();
        int switchNumberInt = Integer.parseInt(switchNumber);

        String str = br.readLine();
        StringTokenizer s = new StringTokenizer(str, " ");

        ArrayList<String> switchList = new ArrayList<>();

        // 토큰을 ArrayList에 저장합니다.
        while (s.hasMoreTokens()) {
            switchList.add(s.nextToken());
        }


        String studentNumber = br.readLine();
        int studentNumberInt = Integer.parseInt(studentNumber);

        for (int i = 0; i < studentNumberInt; i++) {
            String student = br.readLine();
            StringTokenizer st = new StringTokenizer(student, " ");
            int gender = Integer.parseInt(st.nextToken());
            int switchIndex = Integer.parseInt(st.nextToken());
            if (gender == 1) {
                for (int j = switchIndex; j <= switchNumberInt; j += switchIndex) {
                    if (switchList.get(j - 1).equals("1")) {
                        switchList.set(j - 1, "0");
                    } else {
                        switchList.set(j - 1, "1");
                    }
                }
            } else if (gender == 2) {
                int left = switchIndex - 1;
                int right = switchIndex + 1;
                String initialSwitch = switchList.get(switchIndex-1);
                if (initialSwitch.equals("1")) {
                    switchList.set(switchIndex-1, "0");
                } else {
                    switchList.set(switchIndex-1, "1");
                }
                while (0 <= left - 1 && right - 1 < switchNumberInt) {
                    String leftSwitch = switchList.get(left - 1);
                    String rightSwitch = switchList.get(right - 1);
                    if (leftSwitch.equals(rightSwitch)) {
                        if (leftSwitch.equals("0")) {
                            switchList.set(left - 1, "1");
                            switchList.set(right - 1, "1");
                        } else {
                            switchList.set(left - 1, "0");
                            switchList.set(right - 1, "0");
                        }
                    }
                    else{
                        break;
                    }
                    left -= 1;
                    right += 1;
                }
            }
        }

        for (int i = 1; i < switchNumberInt+1; i++) {
            System.out.print(switchList.get(i-1)+" ");
            if (i%20==0){
                System.out.println();
            }
        }
    }
}
