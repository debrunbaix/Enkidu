
void _FINI_0(void)

{
  if (DAT_003015e8 == '\0') {
    if (PTR___cxa_finalize_00300ff8 != (undefined *)0x0) {
      __cxa_finalize(PTR_LOOP_00301008);
    }
    FUN_00100720();
    DAT_003015e8 = 1;
    return;
  }
  return;
}

