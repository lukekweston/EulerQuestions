fun main() {
    var sum = 0
    for(i in 1..1000000){
        if(i.toString(2) == i.toString(2).reversed() && i.toString() == i.toString().reversed()){
            sum += i
        }
    }
    println("Result: $sum")
}