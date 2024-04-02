function solution(maps) {
    const n = maps.length;
    const m = maps[0].length;
    
    const dx = [-1, 1, 0, 0]; // 상, 하, 좌, 우
    const dy = [0, 0, -1, 1];
    
    const queue = [[0, 0, 1]]; // 시작 지점 (0, 0), 거리 1로 초기화
    const visited = Array.from({length: n}, () => Array(m).fill(0)); // 방문 여부를 저장하는 배열
    
    while (queue.length > 0) {
        const [x, y, dist] = queue.shift();
        
        // 상대 팀 진영에 도착한 경우
        if (x === n - 1 && y === m - 1) {
            return dist;
        }
        
        // 상, 하, 좌, 우로 이동하는 경우를 탐색
        for (let i = 0; i < 4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];
            
            // 이동 가능한 범위 내에서
            if (0 <= nx && nx < n && 0 <= ny && ny < m && maps[nx][ny] === 1 && visited[nx][ny] === 0) {
                visited[nx][ny] = 1;
                queue.push([nx, ny, dist + 1]);
            }
        }
    }
    
    // 상대 팀 진영에 도달할 수 없는 경우
    return -1;
}
