function solution(babbling) {
    var answer = 0;
    
    var arr = ["aya", "ye", "woo", "ma"];
    
    babbling.forEach(o => {
        var o_length = o.length
        var e_length = 0;
        arr.forEach(e => {
            e_length = e.length
            if (o.indexOf(e) != -1){
                o_length -= e_length;
            }
        })

        if(o_length == 0){answer+=1;}
    })
    
    return answer;
}
