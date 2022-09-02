/* eslint-disable no-prototype-builtins */
/* eslint-disable no-restricted-syntax */
/**
 * 각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다
 * 신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
 * 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
 * k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
 *
 * 구해야하는 것 : 각 유저가 신고한 사람의 정지 처리가 된 횟수
 * 주어지는 것 : 유저 목록, 유저 신고 목록, 정지 기준 횟수
 *
 * 1. report에서 신고당한 유저를 오브젝트로 만든다.({frodo: 2, neo : 2 ,...})
 * 2. 신고당한 유저 오브젝트에서 value가 k보다 크거나 같으면 정지 리스트에 넣는다.
 * 3. report에서 신고를 한 사람이 정지 리스트에 있는 사람을 신고했는지 확인 후 있다면 있는만큼 카운트를한다.
 */
// ㅠㅠ...지문에 있는 테스트 유형은 통과하지만... 채점에서 장렬히 실패한 코드입ㄴ디ㅏ.
// 밑에 정답코드 있습니다!
// 이전에 풀었었는데 이 문제는 다시 풀어봐야할 것 같습니다!
const declaration = (report) => {
  const setReport = new Set(report);
  const uniqueReport = [...setReport];

  const declarationObj = uniqueReport.reduce((acc, cur) => {
    const declarationUser = cur.split(' ')[1];

    if (acc.hasOwnProperty(declarationUser)) {
      acc[declarationUser] += 1;
    } else {
      acc[declarationUser] = 1;
    }

    return acc;
  }, {});

  return declarationObj;
};

const suspension = (users, standard) => {
  const suspensedUser = [];

  for (const key in users) {
    if (users[key] >= standard) {
      suspensedUser.push(key);
    }
  }

  return suspensedUser;
};

const solution = (idList, report, k) => {
  const declarationUsers = declaration(report);
  const suspensedUser = suspension(declarationUsers, k);

  const reports = report.reduce((acc, cur) => {
    const reportedUser = cur.split(' ')[0];
    const declarationUser = cur.split(' ')[1];

    if (suspensedUser.indexOf(declarationUser) !== -1) {
      if (acc.hasOwnProperty(reportedUser)) {
        acc[reportedUser] += 1;
      } else {
        acc[reportedUser] = 1;
      }
    }

    return acc;
  }, {});

  const result = idList.map((v) => {
    if (reports.hasOwnProperty(v)) {
      return reports[v];
    }

    return 0;
  });

  return result;
};

describe('신고 결과 받기', () => {
  it('신고한 사람이 정지되었으면 카운트합니다.', () => {
    expect(
      solution(
        ['con', 'ryan'],
        ['ryan con', 'ryan con', 'ryan con', 'ryan con'],
        3,
      ),
    ).toEqual([0, 0]);
  });
  it('유저 아이디와 신고 횟수를 반환합니다.', () => {
    expect(
      declaration(['ryan con', 'ryan con', 'ryan con', 'ryan con']),
    ).toEqual({ con: 1 });
  });
  it('유저의 신고 횟수가 기준보다 크거나 같다면 해당 유저를 배열에 담아 반환합니다.', () => {
    expect(suspension({ frodo: 2, neo: 2, muzi: 1 }, 2)).toEqual([
      'frodo',
      'neo',
    ]);
  });
});

// 이 전에 풀었던 정답코드입니다...!
// function solution(id_list, report, k) {
//   const setReport = [...new Set(report)];
//   const out = [];
//   const count = Array(id_list.length).fill(0);
//   const mail = Array(id_list.length).fill(0);

//   for (const x of setReport) {
//     const reporter = x.split(' ')[0];
//     const reported = x.split(' ')[1];
//     const idxReported = id_list.indexOf(reported);

//     count[idxReported] += 1;

//     if (count[idxReported] >= k) {
//       out.push(id_list[idxReported]);
//     }
//   }

//   setReport.map((x, idx) => {
//     const reporter = x.split(' ')[0];
//     const reported = x.split(' ')[1];

//     if (out.indexOf(reported) >= 0) {
//       const idx = id_list.indexOf(reporter);
//       mail[idx] += 1;
//     }
//   });

//   return mail;
// }
