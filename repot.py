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

    def create_post(self, author, title, content):
        if author in self.members:
            new_post = Post(title, content, author)
            self.posts.append(new_post)
            print("-" * 50)
            print(f"{author}님, 새로운 게시글이 작성되었습니다.")
            print("-" * 50)
        else:
            print("-" * 80)
            print(f"{author}님은 등록된 회원이 아닙니다. 먼저 회원가입을 진행해주세요.")
            print("-" * 80)

    def display_members(self):
        print("-" * 30)
        print("\n회원 목록:")
        if not self.members:
            print("등록된 회원이 없습니다.")
        else:
            for username, member in self.members.items():
                print(f"이름: {member.name}, 아이디: {username}")
        print("-" * 30)

    def display_posts(self):
        print("-" * 30)
        print("\n게시글 목록:")
        if not self.posts:
            print("등록된 게시글이 없습니다.")
        else:
            for post in self.posts:
                print(f"제목: {post.title}, 작성자: {post.author}")
                print(f"내용: {post.content}")
        print("-" * 30)


membership_system = MembershipSystem()

while True:
    print("\n1. 회원가입\n2. 회원 목록 조회\n3. 게시글 작성\n4. 게시글 목록 조회\n5. 종료")
    choice = input("번호를 선택 해주세요: ")

    if choice == '1':
        name = input("이름을 입력하세요: ")
        username = input("아이디를 입력하세요: ")
        password = input("비밀번호를 입력하세요: ")
        membership_system.register_member(name, username, password)

    elif choice == '2':
        membership_system.display_members()

    elif choice == '3':
        if not membership_system.members:
            print("등록된 회원이 없습니다. 먼저 회원가입을 진행해주세요.")
        else:
            author = input("게시글을 작성할 회원의 아이디를 입력하세요: ")
            title = input("게시글 제목을 입력하세요: ")
            content = input("게시글 내용을 입력하세요: ")
            membership_system.create_post(author, title, content)

    elif choice == '4':
        membership_system.display_posts()

    elif choice == '5':
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 선택이 아닙니다. 다시 선택해주세요.")
