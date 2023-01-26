class Team {
  constructor(sno,team,won,draw,lost, team_won,team_draw,team_lost) {
    this.rank = 0;
    this.sno = sno ;
    this.team = team ;
    this.games = won + draw + lost ;
    this.won = won ;
    this.draw = draw ;
    this.lost = lost ;
    this.team_games = team_won + team_draw + team_lost ;
    this.team_won = team_won ; 
    this.team_draw = team_draw ; 
    this.team_loss = team_lost ; 
    this.tb1 = won + draw * 0.5 ;
    this.tb2 = team_won*2 , team_draw * 1 ;
    this.tb3 = 0 ;  
    let this.opponents = [];
  }
}

let JohnCena = new Team(1,"Ur mum",4,2,6,3,7,8);
let Rick = new Team(2,"WHEEEEEEEEE",4,2,6,3,9,8);
let Why = new Team(3,"Gae",4,2,6,3,4,6);
let participants = [JohnCena,Rick,Why];


participants.sort((a, b) => {
    if (a.tb1 > b.tb1)
        return -1;
    if (a.tb1 < b.tb1)
        return 1;
    if (a.tb1 == b.tb1){
      if (a.tb2 > b.tb2)
        return -1;
      if (a.tb2 < b.tb2)
        return 1;
      
      
    }
    return 0;
});




let table = document.querySelector('table');

let x = 0;
while (x <= participants.length){
participants[x].rank = x+1 ;


let template = `
                <tr>
                    <td style="text-align: center">${participants[x].rank}</td>
                    <td style="text-align: center">${participants[x].sno}</td>
                    <td style="text-align: center">${participants[x].team}</td>
                    <td style="text-align: center">${participants[x].games}</td>
                    <td style="text-align: center">${participants[x].won}</td>
                    <td style="text-align: center">${participants[x].draw}</td>
                    <td style="text-align: center">${participants[x].lost}</td>
                    <td style="text-align: center">${participants[x].team_games}</td>
                    <td style="text-align: center">${participants[x].team_won}</td>
                    <td style="text-align: center">${participants[x].team_draw}</td>
                    <td style="text-align: center">${participants[x].team_lost}</td>
                    <td style="text-align: center">${participants[x].tb1}</td>
                    <td style="text-align: center">${participants[x].tb2}</td>
                    <td style="text-align: center">${participants[x].tb3}</td>
                    
                </tr>`;
table.innerHTML += template;
x ++ ;
 
}
