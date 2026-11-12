// Создаёт пользователя admin/admin при первом запуске (только для демо!).
import jenkins.model.*
import hudson.security.*

def instance = Jenkins.get()

def realm = new HudsonPrivateSecurityRealm(false)
realm.createAccount(
    System.getenv('JENKINS_ADMIN_ID') ?: 'admin',
    System.getenv('JENKINS_ADMIN_PASSWORD') ?: 'admin'
)
instance.setSecurityRealm(realm)

def strategy = new FullControlOnceLoggedInAuthorizationStrategy()
strategy.setAllowAnonymousRead(false)
instance.setAuthorizationStrategy(strategy)

instance.save()
println ">>> Demo admin user created"
