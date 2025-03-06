package com.mycompany.aulapoo;

import java.util.UUID;

public class Caneta {
    public String Color;
    public boolean IsClosed;
    public int Charge;
    private String Model;
    private UUID SerialNumber;
    
    public Caneta(String color, boolean isClosed, int charge, String model, UUID serialNumber)
    {
        this.Color = color;
        this.IsClosed = isClosed;
        this.Charge = charge;
        this.Model = model;
        this.SerialNumber = serialNumber;
    }
    
    public String GetModel()
    {
        return this.Model;
    }
    
    public UUID GetSerialNumber()
    {
        return this.SerialNumber;
    }
    
    public void SetModel(String model)
    {
        this.Model = model;
    }
    
    public void SetSerialNumber(UUID serialNumber)
    {
        this.SerialNumber = serialNumber;
    }
    
    @Override
    public String toString()
    {
        return String.format("Modelo da Caneta: %s, Número de Série : %s, Cor : %s, Está Tampada ? %b, Qual a carga ? %d", this.Model, this.SerialNumber, this.Color, this.IsClosed, this.Charge);
    }
}
