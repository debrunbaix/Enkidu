
void main(int param_1,undefined4 *param_2)

{
  undefined4 *puVar1;
  void *__dest;
  int iVar2;
  undefined4 *puVar3;
  int in_GS_OFFSET;
  byte bVar4;
  undefined4 local_96 [25];
  char local_32 [30];
  int local_14;
  undefined4 *puStack_10;
  
  puVar1 = param_2;
  bVar4 = 0;
  puStack_10 = &param_1;
  local_14 = *(int *)(in_GS_OFFSET + 0x14);
  if (param_1 != 2) {
    printf("(*) -Syntaxe: %s [password] \n",*param_2);
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  __dest = malloc(0x1d);
  memcpy(__dest,&DAT_08048910,0x1f);
  puVar3 = local_96;
  for (iVar2 = 0x19; iVar2 != 0; iVar2 = iVar2 + -1) {
    *puVar3 = 0;
    puVar3 = puVar3 + (uint)bVar4 * -2 + 1;
  }
  memcpy(local_96,"_Celebration",0xd);
  *(undefined *)((int)__dest + 5) = 99;
  *(undefined *)((int)__dest + 0x16) = 0;
  function_ptr_2175 = WPA;
  strcpy(local_32,(char *)puVar1[1]);
  *(undefined *)((int)__dest + 8) = 0x5f;
  *(undefined *)((int)__dest + 9) = 0x2e;
  (*function_ptr_2175)(local_32,__dest);
  if (local_14 == *(int *)(in_GS_OFFSET + 0x14)) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

