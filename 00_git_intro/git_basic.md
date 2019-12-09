# 마크다운(MarkDown)

> 일반 텍스트 형식 구문을 사용하는 마크업 언어의 일종으로 사용이 쉽고 간결하다.
>
> 단, 모든 HTML 마크업을 대체하지 않는다. (인용구는 shift+>)

## 1.문법

### 1.1 Header

> 헤더는 제목을 표현할 때 사용합니다. 
>
> 단순히 글자의 크기를 나타낼 때 사용하는 것이 아니라 의미론 적인 중요도를 갖습니다. 

-  h1~h6까지 표현이 가능합니다.
- #의 개수로 표현하거나 <h1></h1> 형태로 표현 가능합니다. 

### 1.2 List

> 목록을 나열할 때 사용합니다.
>
> 순서가 필요한 항목과 그렇지 않은 항목으로 구분할 수 있습니다. 
>
> 순서/순서x 항목을 같이 사용할 수 있습니다.

- 순서가 없는 항목
  - 순서가 없는 하위 항목 
  - 순서가 없는 하위 항목

1. (.찍고 + space) 순서가 있는 항목
2. 순서가 있는 항목
   1. (tab-하위항목) 순서가 있는 하위 항목

- 순서가 없는 항목 
  1. 순서가 있는 항목

### 1.3 Code Block

> 코드 블럭은 작성한 코드를 정리하거나 강조하고 싶을 때 사용합니다.
>
> 코드 블럭은 인라인과 블럭 단위로 구분할 수 있습니다. 

- Inline
  - 인라인으로 처리하고 싶은 부분을 `(백틱)으로 감싸줍니다. 

- Block
  - (백틱)을 3번 입력하고` Enter`를 눌러서 생성합니다. 

```bash
$ git add .
$ git commit -m "commit message"
$ git push origin master
```

```css
#style {
    width: 100px;
    height: 80px;
}
```



### 1.4 Image

> 로컬에 있는 이미지를 삽입하거나 이미지 링크를 활용하여 표시합니다.

- `![]()` 를 작성하고 `()`안에 주소를 입력합니다. 
  - 이 때, `[]` 안에는 이미지 이름을 입력합니다.

- 로컬에 있는 이미지 파일을 로드할 때는 절대 경로가 아닌 상대 경로를 사용합니다. 

<img src="https://d22ir9aoo7cbf6.cloudfront.net/wp-content/uploads/sites/4/2019/10/Alila-Seminyak-Coastal-Christmas.jpg" alt="git(christmas)" style="zoom:20%;" />

![](.\images\christmas_image.jpg)



### 1.5 Link

> 특정 주소로 링크를 걸 때 사용합니다. 

- `[]()` 를 작성하고 `()` 안에 링크를 걸 주소를 입력합니다. 

[Slack Page](https://slack.com/intl/en-kr/)



### 1.6 Table

> 표를 작성하여 요소를 구분할 수 있습니다. 

- `|` (파이프) 사이에 컬럼을 작성하고 `Enter`를 입력합니다. 
- 마지막 컬럼을 작성하고 뒤에 `|`를 붙여줍니다.
- (ex) |Working

| Working Directory | Staging Area | Remote Repo |
| ----------------- | ------------ | ----------- |
| working tree      | Index        | history     |
| working copy      | cache        |             |

### 1.7 기타

**인용문** (****가운데에 인용문구 넣으면 볼드 처리 됨)

- `>`를 입력하고 `Enter` 를 누릅니다.

> git은 컴퓨터의 파일 변경 사항을 추적합니다.

- 중첩된 인용문을 사용할 수 있습니다.

> $git add .
>
> > $git commit -m "first commit"

**수평선**

- `---` , `***` ,`___` 를 입력하여 작성합니다.

Working Directory 

---

Staging Area (commit할 목록을 담아두는 area)

___

Remote Repository(Github)

**강조** (ctrl+b하면 자동으로 됨)

- 이탤릭체는 해당 부분을 `*`, `_` 1개로 감싸줍니다.

- 보드체는 해당 부분을 `**`, `__` 2개로 감싸줍니다.
- 취소선은 `~~` 2개로 감싸줍니다.

이것은 *이탤릭체*입니다.

이것은 __보드체__입니다.

이것은 ~~취소선~~입니다. 