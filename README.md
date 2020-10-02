BÀI 1
  DEPTH FIRST SEARCH:  Hoạt động theo cơ chế của stack
    Cho điểm xuất phát ban đầu vào stack 
    Nếu stack rỗng thì tìm kiếm thất bại , kết thúc tìm kiếm
    Nếu đi đến đích (state cuối cùng) thì tìm kiếm thành công, kết thúc tìm kiếm 
  
   
    visited = set() //khai báo set để lưu trạng thái state 
    stack = util.Stack() // khai báo stack 
    stack.push((problem.getStartState(), [])) //push trạng thái ban đầu

    while not stack.isEmpty():  // chừng nào stack còn không rỗng thì thực hiện
        state, actions = stack.pop()

        if state in visited: // nếu state nằm trong visited thì bỏ qua 
            continue

        visited.add(state) // thêm state vào visited 

        if problem.isGoalState(state): // nếu trạng thái là hợp lệ thì pop state ra khỏi stack 
            return actions

        for successor, action, stepCost in problem.getSuccessors(state): // chừng nào successor, action, stepCost còn trong trạng thái để đi đến đích 
            if successor not in visited: // nếu trạng thái điểm tiếp theo không có trong visited thì ta push trạng thái của successor , action vào trong stack 
                stack.push((successor, actions + [action]))

    
