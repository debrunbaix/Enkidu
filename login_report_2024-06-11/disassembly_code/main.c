
/* WARNING: Function: __x86.get_pc_thunk.bx replaced with injection: get_pc_thunk_bx */

undefined4 main(void)

{
  int iVar1;
  char local_1a [6];
  int local_14;
  undefined *local_10;
  
  local_10 = &stack0x00000004;
  local_14 = 0;
  puts("Enter admin password: ");
  gets(local_1a);
  iVar1 = strcmp(local_1a,"pass");
  if (iVar1 == 0) {
    puts("Correct Password!");
    local_14 = 1;
  }
  else {
    puts("Incorrect Password!");
  }
  if (local_14 == 0) {
    printf("Failed to log in as Admin (authorised=%d) :(\n",0);
  }
  else {
    printf("Successfully logged in as Admin (authorised=%d) :)\n",local_14);
  }
  return 0;
}

