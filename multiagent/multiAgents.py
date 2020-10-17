# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        

        # tinh khoang cach den thuc an gan nhat
        newFoodList = newFood.asList()
        min_food_distance = -1

        for food in newFoodList:
          distance = util.manhattanDistance(newPos, food)
          if min_food_distance >= distance or min_food_distance == -1:
            min_food_distance = distance

        # tinh khoang cach cua pacman den cac con ma va kiem tra so con ma co khoang cach = 1 quanh pacman

        distance_to_ghosts = 1
        check_to_ghosts = 0

        for ghostState in successorGameState.getGhostPositions():
          distance = util.manhattanDistance(newPos, ghostState)
          distance_to_ghosts += distance
          if distance <= 1:
            check_to_ghosts += 1

        # kq = diem + 1/(min_food_distance) - 1/(distance_to_ghosts) - check_to_ghosts

        return successorGameState.getScore() + (1 / float(min_food_distance)) - (1 / (distance_to_ghosts)) - check_to_ghosts


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()
        actions = gameState.getLegalActions(0)
        return max(actions,
                   key=lambda x: self.minimax_search(gameState.generateSuccessor(0,x),1))

    def minimax_search(self,gameState,turn):
        numOfAgents = gameState.getNumAgents()
        agentIndex = turn % numOfAgents
        depth = turn // numOfAgents
        if gameState.isWin() or gameState.isLose() or depth == self.depth:
            return self.evaluationFunction(gameState)
        actions= gameState.getLegalActions(agentIndex)
        evals= [self.minimax_search(gameState.generateSuccessor(agentIndex,action),turn+ 1) for action in actions]
        if agentIndex >0:
            return min(evals)
        return max(evals)

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()
        actions = gameState.getLegalActions(0)
        alpha, beta= -999999, 999999
        vals = []
        for action in actions:
            v= self.alphabeta_search(gameState.generateSuccessor(0,action),1,alpha,beta)
            alpha= max(alpha,v)
            vals.append(v)
        for i in range(len(actions)):
            if alpha ==vals[i]:
                return actions[i]
    def alphabeta_search(self, gameState, turn, alpha, beta):
        numOfAgents = gameState.getNumAgents()
        agentIndex = turn % numOfAgents
        depth = turn // numOfAgents
        if gameState.isWin() or gameState.isLose() or depth == self.depth:
            return self.evaluationFunction(gameState)
        actions= gameState.getLegalActions(agentIndex)
        v = -999999 if agentIndex == 0 else 999999
        for action in actions:
            successor = gameState.generateSuccessor(agentIndex, action)
            if agentIndex >0:
                v= min(v,self.alphabeta_search(successor, turn+1, alpha,beta))
                if v< alpha:
                    return v
                beta = min(beta,v)
            else:
                v= max(v, self.alphabeta_search(successor, turn+1, alpha, beta))
                if v> beta:
                    return v
                alpha = max(alpha,v)
        return v

        
class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()
        actions = gameState.getLegalActions(0)
        return max(actions,
                   key=lambda x: self.expectimax_search(gameState.generateSuccessor(0,x),1))
    def expectimax_search(self, gameState, turn):
        numOfAgents = gameState.getNumAgents()
        agentIndex = turn % numOfAgents
        depth = turn // numOfAgents
        if gameState.isWin() or gameState.isLose() or depth == self.depth:
            return self.evaluationFunction(gameState)
        actions= gameState.getLegalActions(agentIndex)
        evals= [self.expectimax_search(gameState.generateSuccessor(agentIndex,action),turn+ 1) for action in actions]
        if agentIndex >0:
            return sum(evals)* 1.0/len(evals)
        return max(evals)

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

