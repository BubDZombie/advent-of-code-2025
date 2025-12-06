{
  for(i=1;i<=NF;i++) {
    problems[i][NR] = $i
  }
}
END {
  num_problems = NF
  operator_index = NR
  sum = 0
  for(i=1; i <= num_problems; i++) {
    operator = problems[i][operator_index]
    answer = 0
    if(operator == "*") {
      answer = 1
    }
    for(j=1; j < operator_index; j++) {
      if(operator == "*") {
        answer = answer * problems[i][j]
      } else {
        answer = answer + problems[i][j]
      }
    }
    sum += answer
  }
  print(sum)
}
