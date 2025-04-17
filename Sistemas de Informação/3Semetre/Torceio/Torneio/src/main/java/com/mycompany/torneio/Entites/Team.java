package com.mycompany.torneio.Entites;

public class Team 
{
    private String Name;
    private int Qtdvictories;
    private int QtdDefeat;
    private int QtdScoredGoals;
    private int QtdConcededGoals;

    public String getName()
    {
        return Name;
    }

    public Team(String name)
    {
        this.Name = name;
        this.Qtdvictories = 0;
        this.QtdDefeat = 0;
        this.QtdScoredGoals = 0;
        this.QtdConcededGoals = 0;
    }
    
    public Team(String Name, int Qtdvictories, int QtdDefeat, int ScoredGoals, int QtdConceded)
    {
        this.Name = Name;
        this.Qtdvictories = Qtdvictories;
        this.QtdDefeat = QtdDefeat;
        this.QtdScoredGoals = ScoredGoals;
        this.QtdConcededGoals = QtdConceded;
    }
    
    public void setName(String Name)
    {
        this.Name = Name;
    }

    public int getQtdvictories()
    {
        return Qtdvictories;
    }

    public void setQtdvictories(int Qtdvictories)
    {
        this.Qtdvictories = Qtdvictories;
    }

    public int getQtdDefeat()
    {
        return QtdDefeat;
    }

    public void setQtdDefeat(int QtdDefeat)
    {
        this.QtdDefeat = QtdDefeat;
    }

    public int getScoredGoals()
    {
        return QtdScoredGoals;
    }

    public void setScoredGoals(int ScoredGoals)
    {
        this.QtdScoredGoals = ScoredGoals;
    }

    public int getQtdConcededGoals()
    {
        return QtdConcededGoals;
    }

    public void setQtdConcededGoals(int QtdConcededGoals)
    {
        this.QtdConcededGoals = QtdConcededGoals;
    }
    
    public void registerVictory(int concededGoals, int ScoredGoals)
    {
        this.Qtdvictories++;
        this.QtdScoredGoals += ScoredGoals;
        this.QtdConcededGoals += concededGoals;
    }
    
    public void registerDefeat(int concededGoals, int ScoredGoals)
    {
        this.QtdDefeat++;
        this.QtdScoredGoals += ScoredGoals;
        this.QtdConcededGoals += concededGoals;
    }
    
    public int GetGoalsDifference()
    {
        return this.QtdScoredGoals - this.QtdConcededGoals;
    }
}   
