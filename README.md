# simple-project
  ეს პროექტი ემსახურება meowfact API-ის დახმარებით მომხმარებელმა სასურველი რაოდენობის საინტერესო ფაქტები და ცნობები მიიღოს კატების შესახებ. პროექტი მოიცავს 5 ძირითად კვანძს(ფუნქციას). ესენია request_cat_facts(), save_into_file(), display_facts(), save_into_database() და main(), რომელშიც გაერთიანებულია ყველა მათგანი.
  request_cat_facts() ფუნქციის დახმარებით ხდება მომხამრებლის მიერ სასურველი რიცხვის შეყვანა, რის შემდეგაც ეს რიცხვითი მნიშვნელობა ჯდება url-ში count-ის ადგილას, რომელიც ფაქტების აღმნიშვნელი პარამეტრია. შემდგომ request ბიბლიოთეკის საშუალებით, ხდება წვდომის გაგზავნა და მიღებული რეზულტატის დამუშავება. ამ ფუნქციაში ერთგვარ ინიციალიზაციას ვუკეთებთ სტატუს კოდს, ჰედერს და შინაარსს(text). API-ს შინაარსიდან გამომდინარე ვერ გამოვიყენე content, რადგან გამოსახულება არ არის მოცემული. ამ ყველაფრის შემდეგ ფუნქციაში მოწმდება სტატუს კოდი, თუ ის დამაკმაყოფილებელია ფუნქცია აბრუნებს json ტიპის მონაცემს, ხოლო თუ სტატუს კოდი არ არის წარმატებული, მაშინ მომხარებელს ატრობინებს ამას.
  save_into_file() ფუნქციში მონაცემებთან წვდომისთვის ვიძახებთ წინა ფუნქციას, ხოლო შემდეგ dump()-ის დახმარებით ამ ინფორმაციას ვწერთ სტრუქტურირებული სახით ფაილში, რომელსაც with open კონსტრუქციის დახმარებით ვხსნით და ვხურავთ.
  Display_facts() ფუნქციის აზრი არის ის რომ, მომხარებლისთვის ნათელი იყოს ის ფაქტები, რომელსაც API-დან ვიღებთ და ფიაილში ვწერთ. ამ ფუნქციის დახმარებით ამ მონაცემების გამოტანა ხდება დანომრილი სახით, რომელიც მის აღქმადობას გაცილებით ამარტივებს.
  save_into_database() ამ ფუნქციის მეშვეობით ხდება დაბრუნებული ფაქტების sqlite ბაზაში შენახვა. ჯერ იქმნება ცხრილი, რომელსაც აქვს id და fact სვეტები. რადგან მონაცემების რაოდენეობის განსაზღვრა წინასწარ შეუძლებელია ვიყენებ executemany-ის. მანამდე კი საერთო ინფორმაციას, რომელიც data ცვლადაში მოქცეული გენერატორის დახმარებით, tuple-ში, ხოლო შემდეგ ისევ ლისტში ვყრი, ანუ ვიღებთ ლისტს, რომელიც tuple-ისგან შედგება.
  main() ფუნქცია წარმოადგენს ერთგვარ თაიგულს, რომელშიც სხვადასხვა ფუნქციებია თავმოყრილი და საბოლოო შედეგი მიიღება
  
