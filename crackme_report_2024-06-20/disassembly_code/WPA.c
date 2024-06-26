
void WPA(char *param_1,char *param_2)

{
  int iVar1;
  
  param_2[0xb] = '\r';
  param_2[0xc] = '\n';
  puts(&DAT_0804893c);
  iVar1 = strcmp(param_1,param_2);
  if (iVar1 == 0) {
    blowfish();
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  RS4();
  puts(&DAT_08048964);
                    /* WARNING: Subroutine does not return */
  exit(1);
}

