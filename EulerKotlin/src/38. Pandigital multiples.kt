//pandigital function takes number to check
//loop 1..9, i remove str(i) from  checked number
//if number.length + i != 9 return false
//return true

fun pandigital(check: String):Boolean{
    var checkEdit = check
    for(i in 1..9){
        checkEdit = checkEdit.replace(i.toString(),"")
        if(checkEdit.length + i != 9){
            return false
        }

    }
    return true
}



fun main() {
    //Create an array list to save pandigital multiples in

    //loop through values 1, (10^5), i
    //loop through 1... j and multiply value by i+j and concat together
        //if length of concatination is less than 9 repeat, if > 9 break if == 9 check if pandigital
        //add to pandigital list
    //print pandigital list max

    var pandigitalVals = arrayListOf<Int>()

    for(i in 1..10000){
        var testVal = ""
        for(j in 1..9){
            testVal += (i * j).toString()
            if(testVal.length > 9){
                break
            }
            if(testVal.length == 9 && pandigital(testVal)){
                pandigitalVals.add(testVal.toInt())


            }
        }
    }

    println("Max: ${pandigitalVals.maxOrNull() ?: 0}")

}