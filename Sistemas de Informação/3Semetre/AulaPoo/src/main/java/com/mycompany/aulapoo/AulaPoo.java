package com.mycompany.aulapoo;
import java.util.UUID;

public class AulaPoo 
{
    public static void main(String[] args) 
    {
        Caneta pencil = new Caneta("Red", true, 5, "Bic", UUID.randomUUID());
        
        System.out.println(pencil);
    }
}
