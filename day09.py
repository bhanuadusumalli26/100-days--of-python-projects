import os

def clear():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

logo='''  

                             .ee.
                     d"  "*$"    "c....
                   .F      ^c      $   *.
                """"*b      3      3F    .
              4       "     4      4"     c
                       b    J      @      $"*e
            .d$b.      $    F     d      .%  ^b
          4*    ^$     $   4     $      ."    ^.
          %       *    $   F   .P     .P       F
         4         r   $  J   zP    e*         L
         $  .      *   $  $  z"  .d"          d"*c
         d"  ^*e    r  $  $.z$..d"        .ed*   "r
        P       *.  *  4 e*"    *.  .ze$$*""      *
       J         ^c  $ ."        ^$"              4
       $           $ *$F         %.b .            "
       ^ .d**$e.    *c$           .$F "*$e.      d
        $      ^*e    $           'd$.     "*bd*"
                  ^*e.$           $$$^*
                      '.         4 3F  ^c
            .....   ..d$         $e$'.   *        d
        c .@"     """   $.   .  ez$F 3    "c     z
         *"           .$""$c. $$$" $  *     $$e$*F
         J       .ze$*"   d" 3" 4  4   *         $
         *     d*"      .P   $  J   F   b        $
         '    P        $"   4   P   b    b      z
          *  d       e"     "   %   $     "e..zP
           "e$      P      F   4    '         $
             ^     $      d    $     b
              b  c F      %    $      c     ."
               b.  $     4     $       *$$$*"
                ^***.    *.    $r    -^ 4
                    ^c    $ .   3.     .P
                      *$$***b    $*=..$"  Gilo94'
                              "*"
                              '''
print(logo)
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid: 
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = (input("Are there any other bidders? Type 'yes' or 'no'.\n")).lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
