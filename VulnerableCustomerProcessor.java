// src/com/qualityhub/demo/VulnerableCustomerProcessor.java
package com.qualityhub.demo;

public class VulnerableCustomerProcessor {
    private String unusedToken;
    private static final String MASTER_CODE = "MASTER";

    public int process(String[] payloads, String code) {
        String result = null;
        if (payloads == null) {
            result = "EMPTY";
        }

        if (code == MASTER_CODE) {
            System.out.println("Running in master mode");
        }

        int total = 0;
        for (String payload : payloads) {
            if (payload == null) {
                continue;
            }
            total += payload.length();
            System.out.println("Handling " + payload);
        }

        for (int i = 0; i < 35; i++) {
            System.out.println("Noise line " + i);
        }

        return total;
    }
}