# Typescript interface

## 인터페이스 vs 타입
latest 버전의 tslint에서 어느정도 가이드를 잡아준다.
- Use an interface instead of a type literal.tslint(interface-over-type-literal)
- 그렇다. Type은 리터럴 값에만 사용하고, Object 형태의 타입을 잡아줄 때는 interface를 사용하면 고민없이 행복해진다.

```typescript
export type AType = 'a' | 'b'

export interface InterA {
  name: string
  age: number
}
```

## 인터페이스 컨벤션

UpperCamelCase
- 자세한 내용은 공식 독스 참조

## 인터페이스 모듈화

```typescript
export interface FormDataList {
  [key: string]: FormDataListItem
}

export interface FormDataListItem {
  label: string
  type: string
  value: string
  placeholder: string
  errors: {
    [key: string]: string | undefined
  }
  validator?: (param: ValidateParam) => ValidateData
  message?: string
}

export interface ValidateParam {
  key: string
  value: string
  form: any
}

export interface ValidateData {
  key: string
  type: string
  status: boolean
  message?: string
}
```
위와 같이 모듈을 만들어 둔 뒤 `import { interfaceName }`으로 가져다 쓰면 된다.

## 인터페이스의 요소로 ?를 사용할 때의 주의점

`message?: string` 와 같이 사용할 경우, message는 string 혹은 undefined가 될 수 있다.

이 경우, Object[string] 같은 탐색이 불가능해진다. undefined 형식으로는 하지 못한다는 에러가 발생할 것이다.

따라서 if 문으로 undefined가 아닐 경우에 탐색하도록 락을 걸어줘야 정상적으로 작동한다. 아래는 그 예외처리의 예시를 사용한 함수이다.

```typescript
const handleUpdateValidate = (data: ValidateData) => {
      const { key, type, status, message } = data
      // message와 같이 undefined로 올 수도 있는 경우, 체크를 잘 해주어야 함
      if (!status && message) {
        formData[key].errors[type] = message
      } else {
        delete formData[key].errors[type]
      }
    }
```
