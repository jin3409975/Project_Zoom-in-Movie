<template>
    <div class="backSize mainBackColor">
        <div class="mypage-container">
            <div class="mypage-header">
                <img class="mypage-avatar" src="https://assets.request-support.com/images/no_profile.gif?ver=1" alt="Profile Avatar">
                <h1 class="listTitle">프로필 변경</h1>
            </div>
            <form class="mypage-form">
                <label for="username">사용자명</label>
                <input type="text" id="username" v-model="user.name">
                
                <label for="language">언어</label>
                <select id="language" v-model="user.language">
                    <option>한국어</option>
                    <option>추가할 예정입니다.</option>
                    <!-- 다른 언어 옵션 추가 가능 -->
                </select>
                
                <!-- 다른 입력 필드 추가 가능 -->
                
                <div class="settings">
                    <h2>개인 정보 설정:</h2>
                    <p>모든 설정을 이 메뉴에서는 모든 환경설정의 모두가 변경됩니다.</p>
                    <button type="button">수정</button>
                </div>
                
                <div class="notifications">
                    <h2>알림 설정:</h2>
                    <p>
                        <input type="checkbox" v-model="user.notifications.email">
                        모든 이메일에서 사이트의 모든 활동 정보 제공
                    </p>
                    <p>
                        <input type="checkbox" v-model="user.notifications.push">
                        모든 디바이스에서 푸시 알림 기기로 제공
                    </p>
                </div>
                
                <div class="actions">
                    <button type="submit">저장</button>
                    <button type="button">취소</button>
                </div>
            </form>
        </div>
    </div>
</template>
  
  <script>
  export default {
    data() {
      return {
        user: {
          name: '',
          language: '한국어',
          notifications: {
            email: false,
            push: false
          }
        }
      };
    },
    methods: {
      saveSettings() {
        // 설정 저장 로직 구현
      }
    }
  };
  </script>
  
  <style scoped>

  label {
    color: white;
  }
  .mypage-container {
    max-width: 600px;
    margin: auto;
    padding: 20px;
    border-radius: 8px;
  }
  
  .mypage-header {
    text-align: center;
    margin-bottom: 30px;
  }
  
  .mypage-avatar {
    width: 80px;
    height: 80px;
    border-radius: 40px;
  }
  
  .mypage-form {
    display: flex;
    flex-direction: column;
  }
  
  .mypage-form label {
    margin-top: 10px;
  }
  
  .mypage-form input[type="text"],
  .mypage-form select {
    padding: 10px;
    margin-top: 5px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  
  .settings, .notifications {
    margin-top: 30px;
    background-color: #fff;
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  
  .actions {
    display: flex;
    justify-content: space-between;
    margin-top: 30px;
  }
  
  .actions button {
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .actions button[type="submit"] {
    background-color: #007bff;
    color: white;
  }
  
  .actions button[type="button"] {
    background-color: #6c757d;
    color: white;
  }
  </style>
  