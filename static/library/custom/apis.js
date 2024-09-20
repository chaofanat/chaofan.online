

// const api_prefix = '/api/v1/objectstorage/';
// const api_urls = {
//     files: {
//         list: api_prefix + 'files/',
//         detail: api_prefix + 'files/:id',
//         create: api_prefix + 'files/',
//         update: api_prefix + 'files/:id',
//         delete: api_prefix + 'files/:id',
//     }
    
// }

// 请求函数封装
const request = function(config, beforeGuard, success, errorCallback) {
    // 守卫：请求前的检查
    if (typeof beforeGuard === 'function') {
        beforeGuard();
    }

    // 获取 token 并检查有效性
    const token = getToken();
    if (!token) {
        console.error('未找到 token，请检查是否已登录');
        return;
    }

    // 构建请求头
    const headers = {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
    };

    // 创建 AbortController 用于请求超时
    const controller = new AbortController();
    const { signal } = controller;

    setTimeout(() => {
        controller.abort();
    }, 5000); // 设置请求超时时间为 5 秒

    // 发起请求
    fetch(config.url, {
        method: config.method,
        headers: headers,
        body: config.method === 'GET' ? undefined : JSON.stringify(config.data),
        signal: signal
    })
    .then(response => {
        if (!response.ok) {
            if (response.status === 401) {
                // 未授权，尝试自动刷新 token
                return refreshToken().then(newToken => {
                    token = newToken;
                    headers['Authorization'] = `Bearer ${newToken}`;
                    return fetch(config.url, {
                        method: config.method,
                        headers: headers,
                        body: config.method === 'GET' ? undefined : JSON.stringify(config.data),
                        signal: signal
                    });
                }).catch(() => {
                    handleUnauthorized();
                });
            } else {
                throw new Error(`请求失败: ${response.status}`);
            }
        }
        return response.json();
    })
    .then(data => {
        // 守卫：请求成功后的处理
        if (typeof success === 'function') {
            success(data);
        }
    })
    .catch(fetchError => {
        // 守卫：请求错误后的处理
        let errorMessage = '请求出错';
        if (fetchError.name === 'AbortError') {
            errorMessage = '请求超时';
        } else if (fetchError instanceof SyntaxError) {
            errorMessage = 'JSON 解析错误';
        } else if (fetchError.message.includes('Failed to fetch')) {
            errorMessage = '网络错误';
        }

        if (typeof errorCallback === 'function') {
            errorCallback(errorMessage, fetchError);
        } else {
            console.error(errorMessage, fetchError);
        }
    });
};

// 获取 token 的函数
function getToken() {
    // 示例：从本地存储或其他地方获取 token
    return localStorage.getItem('token') || '';
}

// 刷新 token 的函数
function refreshToken() {
    // 示例：从服务器获取新的 token
    return fetch('https://api.example.com/refresh-token')
        .then(response => {
            if (!response.ok) {
                throw new Error(`刷新 token 失败: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            localStorage.setItem('token', data.token);
            return data.token;
        });
}

// 处理未授权的情况
function handleUnauthorized() {
    // 示例：重新获取 token 或提示用户重新登录
    console.log('未授权，请重新登录');
}

//  示例请求配置
// const requestConfig = {
//     url: 'https://api.example.com/data',
//     method: 'GET',
//     data: {}
// };

// 示例使用
const beforeGuard = () => {
    console.log('请求前的守卫');
};

const success = data => {
    console.log('请求成功:', data);
};

const errorCallback = (errorMessage, error) => {
    console.log('请求错误:', errorMessage, error);
};

// 发起请求
// request(requestConfig, beforeGuard, success, errorCallback);








