const params = location.search.slice(1);
export default {
  startYear: 2019,
  secPerMonth: 10,
  schoolTimeSpeedup: 20,
  monthlyExpenses: 1000,
  retirementAge: 65,
  retirementSavingsMin: 500000,
  gameOverBalance: -10000,
  deepeningAutomationAlpha: 0.05,
  newRobotSkillMinImportance: 0.03,
  startingJobs: [428, 721, 333, 717],
  applicationMinMonths: 1,
  loanTerms: {
    interestRate: 0.058,
    years: 10
  },

  // <https://www.bankrate.com/finance/taxes/tax-brackets.aspx>
  taxBrackets: [{
    amount: 13600,
    rate: 0.1
  }, {
    amount: 51800,
    rate: 0.12
  }, {
    amount: 82500,
    rate: 0.22
  }, {
    amount: 157500,
    rate: 0.24
  }, {
    amount: 200000,
    rate: 0.32
  }, {
    amount: 500000,
    rate: 0.35
  }, {
    amount: 100000000,
    rate: 0.37
  }],

  // Work minigame
  maxSkillChangePerWork: 0.001,
  workPerClick: 7,
  slackPerFrame: 1,
  minSlackPerFrame: 0.02,

  debug: params.includes('debug'),
  perfectApplicant: false,
  startHighSchool: false
};
