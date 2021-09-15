interface validateResult {
  status: boolean
  message: string
  check?: boolean
}

export const emailValidator = (key: string, value: string): validateResult => {
  return { status: true, message: 'hi' }
}
