    public void run()
    {
        for (int i = 0; i < 4; i++) {

            String theUser = readLine("Enter your choice (rock, paper, or scissors):");
            System.out.println("User:" + theUser);
            int computerNumber= Randomizer.nextInt(0, 2);
            if(computerNumber == 0)
                theComputer = "rock";
            else if(computerNumber == 1)
                theComputer = "paper";
            else
                theComputer = "scissors";
            System.out.println("Computer: " + theComputer);
            System.out.println(getWinner(theUser, theComputer));
        }
        System.out.println("Thanks for playing!");
    }
