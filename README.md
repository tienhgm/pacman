BÀI 1
  DEPTH FIRST SEARCH( tìm kiếm theo chiều sâu):  Hoạt động theo cơ chế của stack
    Cho điểm xuất phát ban đầu vào stack 
    Nếu stack rỗng thì tìm kiếm thất bại , kết thúc tìm kiếm 
    Trong quá trình đó ta lưu từng hành động qua từng trạng thái cho đến đích vào list của từng phần tử trong Stack, một list khác không nằm trong Stack dùng để lưu những vị trí       đã được duyệt nhằm không duyệt trùng lặp.
    Nếu đi đến đích (state cuối cùng) thì tìm kiếm thành công, kết thúc tìm kiếm 
  
   

Bài 2 
    BREATH FIRST SEARCH( tìm kiếm theo chiều rộng): Hoạt động theo cơ chế của queue
      Cho điểm xuất phát ban đầu vào queue
      Nếu queue rỗng thì tìm kiếm thất bại , kết thúc tìm kiếm
      Trong quá trình đó ta lưu từng hành động qua từng trạng thái cho đến đích vào list của từng phần tử trong queue, một list khác không nằm trong queue dùng để lưu những vị           trí đã được duyệt nhằm không duyệt trùng lặp.
      Nếu đi đến đích (state cuối cùng) thì tìm kiếm thành công, kết thúc tìm kiếm
        
        
Bài 3 
     UNIFORM COST SEARCH:
        Cho điểm xuất phát ban đầu vào PriorityQueue
        Nếu PriorityQueue rỗng thì tìm kiếm thất bại , kết thúc tìm kiếm
        Ta sử dụng Priority Queue với độ ưu tiên là tổng giá trị các bước để đi đến trạng thái đích, tổng giá trị nào nhỏ hơn thì sẽ được ưu tiên xếp lên đầu của hàng đợi.
        Cho đến khi đến được trạng thái đích với tổng giá trị nhỏ nhất thì kết thúc tìm kiếm 
  
Bài 4
     aStarSearch:
        Cho điểm xuất phát ban đầu vào PriorityQueue
        Nếu PriorityQueue rỗng thì tìm kiếm thất bại , kết thúc tìm kiếm
        Ta sử dụng Priority Queue với độ ưu tiên là tổng giá trị các bước để đi đến trạng thái đích, tổng giá trị nào nhỏ nhất cộng với việc thêm ước tính đến trạng thái gần nhất         đạt giá trị nhỏ nhất thì xếp lên đầu hàng đợi 
        Cho đến khi tìm được trạng thái đích thỏa mãn yêu cầu thì kết thúc tìm kiếm 
        
