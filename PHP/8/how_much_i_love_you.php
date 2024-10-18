function how_much_i_love_you(int $nb_petals): string {
  $suz = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"];
  return $suz[($nb_petals-1)%6];
}


echo how_much_i_love_you(8)  # result: I love you
