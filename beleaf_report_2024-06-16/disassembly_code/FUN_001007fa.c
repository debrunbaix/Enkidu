
long FUN_001007fa(char param_1)

{
  long local_10;
  
  local_10 = 0;
  while ((local_10 != -1 && ((int)param_1 != *(int *)(&DAT_00301020 + local_10 * 4)))) {
    if ((int)param_1 < *(int *)(&DAT_00301020 + local_10 * 4)) {
      local_10 = local_10 * 2 + 1;
    }
    else if (*(int *)(&DAT_00301020 + local_10 * 4) < (int)param_1) {
      local_10 = (local_10 + 1) * 2;
    }
  }
  return local_10;
}

