(module
  (memory 1)
  (export "memory" (memory 0))

  (global $state (mut i32) (i32.const 0))

  (func (export "set_state") (param $v i32)
    local.get $v
    global.set $state
  )

  (func (export "get_state") (result i32)
    global.get $state
  )
)
