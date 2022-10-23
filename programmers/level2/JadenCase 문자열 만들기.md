# JadenCase 문자열 만들기

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12951)

```java
import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(String s) {
        StringBuilder builder = new StringBuilder();
        String[] strs = s.toLowerCase().split("");
        boolean isBlank = true;
        
        for (String str : strs) {
            builder.append(isBlank ? str.toUpperCase() : str);
            isBlank = str.equals(" ");
        }
        
        return builder.toString();
    }
}
```