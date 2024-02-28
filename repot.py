class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


class MembershipSystem:
    def __init__(self):
        self.members = {}
        self.posts = []
        self.current_user = None  # 현재 로그인한 사용자

    def register_member(self, name, username, password):
        if username in self.members:
            print("-" * 55)
            print("이미 존재하는 아이디입니다. 다른 아이디를 사용해주세요.")
            print("-" * 55)
        else:
            new_member = Member(name, username, password)
            self.members[username] = new_member
            print("-" * 34)
            print(f"{name}님, 회원가입을 축하합니다.")
            print("-" * 34)

    def login(self, username, password):
        if username in self.members and self.members[username].password == password:
            self.current_user = self.members[username]
            print("-" * 40)
            print(f"{self.current_user.name}님, 환영합니다. 로그인되었습니다.")
            print("-" * 40)
        else:
            print("-" * 50)
            print("아이디 또는 비밀번호가 올바르지 않습니다.")
            print("-" * 50)

    def create_post(self, title, content):
        if self.current_user:
            new_post = Post(title, content, self.current_user.username)
            self.posts.append(new_post)
            print("-" * 50)
            print(f"{self.current_user.name}님, 새로운 게시글이 작성되었습니다.")
            print("-" * 50)
        else:
            print("-" * 50)
            print("로그인이 필요합니다. 먼저 로그인을 진행해주세요.")
            print("-" * 50)

    def display_members(self):
        print("-" * 30)
        print("\n회원 목록:")
        if not self.members:
            print("등록된 회원이 없습니다.")
        else:
            for username, member in self.members.items():
                print(f"이름: {member.name}, 아이디: {username}")
        print("-" * 30)

    def display_posts(self, search_word=None):
        print("-" * 30)
        print("\n게시글 목록:")
        if not self.posts:
            print("등록된 게시글이 없습니다.")
        else:
            for post in self.posts:
                if search_word is None or search_word.lower() in post.content.lower() or search_word.lower() in post.title.lower():
                    print("-" * 30)
                    print(f"제목: {post.title}, 작성자: {post.author}")
                    print(f"내용: {post.content}")
        print("-" * 30)


membership_system = MembershipSystem()

while True:
    print("\n1. 회원가입\n2. 로그인\n3. 회원 목록 조회\n4. 게시글 작성\n5. 게시글 목록 조회\n6. 게시글 검색\n7. 종료")
    choice = input("번호를 선택하세요: ")

    if choice == '1':
        name = input("이름을 입력하세요: ")
        username = input("아이디를 입력하세요: ")
        password = input("비밀번호를 입력하세요: ")
        membership_system.register_member(name, username, password)

    elif choice == '2':
        username = input("아이디를 입력하세요: ")
        password = input("비밀번호를 입력하세요: ")
        membership_system.login(username, password)

    elif choice == '3':
        membership_system.display_members()

    elif choice == '4':
        if not membership_system.current_user:
            print("-" * 50)
            print("로그인이 필요합니다. 먼저 로그인을 진행해주세요.")
            print("-" * 50)
        else:
            title = input("게시글 제목을 입력하세요: ")
            content = input("게시글 내용을 입력하세요: ")
            membership_system.create_post(title, content)

    elif choice == '5':
        membership_system.display_posts()

    elif choice == '6':
        search_word = input("검색할 단어를 입력하세요: ")
        membership_system.display_posts(search_word)

    elif choice == '7':
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 선택이 아닙니다. 다시 선택해주세요.")
        
