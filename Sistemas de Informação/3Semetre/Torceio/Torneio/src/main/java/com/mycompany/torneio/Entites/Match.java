package com.mycompany.torneio.Entites;

public class Match
{
    private Team HomeTeam;
    private Team VisitingTeam;
    private int QtdGoalsHomeTeam;
    private int QtdGoalsVisitingTeam;
    
    public Match(Team HomeTeam, Team VisitingTeam, int QtdGoalsHomeTeam, int QtdGoalsVisitingTeam)
    {
        this.HomeTeam = HomeTeam;
        this.VisitingTeam = VisitingTeam;
        this.QtdGoalsHomeTeam = QtdGoalsHomeTeam;
        this.QtdGoalsVisitingTeam = QtdGoalsVisitingTeam;
    }
    
    public Team PlayMatch(int qtdGoalsHomeTeam, int qtdGoalsVisitingTeam)
    {
        this.QtdGoalsHomeTeam = qtdGoalsHomeTeam;
        this.QtdGoalsVisitingTeam = qtdGoalsVisitingTeam;
        
        System.out.println(this.HomeTeam.getName() + " " + qtdGoalsHomeTeam + " || " + this.VisitingTeam + " " + qtdGoalsVisitingTeam);
        
        if(qtdGoalsHomeTeam > qtdGoalsVisitingTeam){
            this.HomeTeam.registerVictory(qtdGoalsHomeTeam, qtdGoalsHomeTeam);
            this.VisitingTeam.registerDefeat(qtdGoalsHomeTeam, qtdGoalsHomeTeam);
            return HomeTeam;
        } else {
            this.VisitingTeam.registerVictory(qtdGoalsHomeTeam, qtdGoalsHomeTeam);
            this.HomeTeam.registerDefeat(qtdGoalsHomeTeam, qtdGoalsHomeTeam);
            return VisitingTeam;
        }
    }
}
