
void blowfish(void)

{
  undefined4 uVar1;
  uint uVar2;
  int in_GS_OFFSET;
  uint local_50;
  undefined4 local_44;
  undefined4 local_40;
  undefined4 local_3c;
  undefined4 local_38;
  undefined2 uStack_34;
  undefined auStack_32 [17];
  undefined4 local_21;
  undefined4 local_1d;
  undefined4 local_19;
  undefined4 local_15;
  undefined4 local_11;
  undefined4 local_d;
  undefined local_9;
  undefined4 local_8;
  
  uVar1 = *(undefined4 *)(in_GS_OFFSET + 0x14);
  local_44 = 0x6562696c;
  local_40 = 0xa9c37472;
  local_3c = 0x21;
  local_50 = 0;
  uVar2 = local_50;
  do {
    local_50 = uVar2;
    *(undefined4 *)((int)&local_38 + local_50) = 0;
    uVar2 = local_50 + 4;
  } while (local_50 + 4 < 0x14);
  local_8 = uVar1;
  *(undefined2 *)(auStack_32 + (local_50 - 2)) = 0;
  auStack_32[local_50] = 0;
  local_21 = 0x4763305f;
  local_1d = 0x6d35636a;
  local_19 = 0x54352e5f;
  local_15 = 0x3887c333;
  local_11 = 0xc3304a43;
  local_d = 0x39483980;
  local_9 = 0;
  printf(&DAT_08048998,&local_44);
                    /* WARNING: Subroutine does not return */
  exit(0);
}

